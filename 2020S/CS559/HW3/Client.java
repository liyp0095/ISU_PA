import java.io.*;
import java.net.*;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Signature;
import java.security.SignatureException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.ShortBufferException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Client {
	public static void main(String[] args) throws IOException, Exception {
//		String serverIP = "127.0.0.1";
//		String serverPort = "3000";
//		String clientPrivateKeyFile = "client.key";
//		String serverPublicKeyFile = "server.key.pub";

		if (args.length < 4) {
			System.out.println("Not enough arguments \nUsage: java Client [server ip address] [server port] [client private key] [server public key]");
			return;
		}

		String serverIP = args[0];
	       	int serverPort = Integer.valueOf(args[1]);
		String clientPrivateKeyFile = args[2];
		String serverPublicKeyFile = args[3];
		
		PrivateKey clientPrivateKey = loadPrivateKey(clientPrivateKeyFile, "RSA");
		PublicKey serverPublicKey = loadPublicKey(serverPublicKeyFile, "RSA");
		
		// build a socket and connect to server
		Socket clientSocket = new Socket(serverIP, serverPort);
		DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
		DataInputStream inFromServer = new DataInputStream(clientSocket.getInputStream());
		
		// generate symmetric key K (128bit)
		byte[] key128K = generateSymmetricKey(128);
		byte[] RSAEncryptedKey128K = RSAEncrypt(key128K, serverPublicKey);
		byte[] signatureKey128K = signDigitalSignature(key128K, clientPrivateKey, "SHA512withRSA");
//		System.out.println("Ciphertext of K:\n" + new String(RSAEncryptedKey128K));
//		System.out.println("\nSignature of K:\n" + new String(signatureKey128K));
		System.out.println("Ciphertext of K:\n");
		printBytes(RSAEncryptedKey128K);
		System.out.println("\nSignature of K:\n");
		printBytes(signatureKey128K);
		
		// send to server
		outToServer.writeInt(RSAEncryptedKey128K.length);
		outToServer.write(RSAEncryptedKey128K);
		outToServer.writeInt(signatureKey128K.length);
		outToServer.write(signatureKey128K);
		System.out.println("send complete\n");
		
		// read cipher text and iv from server
		int ciphertextLength = inFromServer.readInt();
		byte[] cipherTextInBytes = new byte[ciphertextLength];
		inFromServer.readFully(cipherTextInBytes);
		
		int ivLength = inFromServer.readInt();
		byte[] ivInBytes = new byte[ivLength];
		inFromServer.readFully(ivInBytes);
		
		// AES decryption
		byte[] decryptedTextInBytes = new byte[ciphertextLength];
		AESDecrypt(decryptedTextInBytes, cipherTextInBytes, key128K, ivInBytes);

		System.out.println("Plaintext:");
		System.out.println(new String(decryptedTextInBytes));
		
	}

	private static void printBytes(byte[] bytes) {
		for (byte b : bytes) {
			System.out.print(b + " ");
		}
	}	
	
	private static byte[] generateSymmetricKey(int length) {
		SecureRandom sr = new SecureRandom();
		byte[] keyInBytes = new byte[length/8];
		sr.nextBytes(keyInBytes);
		return keyInBytes;
	}
	
	private static PublicKey loadPublicKey(String publicKeyFile, String algorithm) throws Exception {
		//Read Public Key from file
		File filePublicKey = new File(publicKeyFile);
		FileInputStream fis = new FileInputStream(publicKeyFile);
		byte[] encodedPublicKey =
		new byte[(int) filePublicKey.length()];
		fis.read(encodedPublicKey);
		fis.close();
		
		KeyFactory keyFactory = KeyFactory.getInstance(algorithm);
		X509EncodedKeySpec publicKeySpec = new X509EncodedKeySpec(encodedPublicKey);
		PublicKey publicKey = keyFactory.generatePublic(publicKeySpec);
		return publicKey;
	}
	
	private static PrivateKey loadPrivateKey(String privateKeyFile, String algorithm) throws Exception {
		//Read Private Key from file
		File filePrivateKey = new File(privateKeyFile);
		FileInputStream fis = new FileInputStream(privateKeyFile);
		byte[] encodedPrivateKey = new byte[(int) filePrivateKey.length()];
		fis.read(encodedPrivateKey);
		fis.close();
		
		KeyFactory keyFactory = KeyFactory.getInstance(algorithm);
		PKCS8EncodedKeySpec privateKeySpec = new PKCS8EncodedKeySpec(encodedPrivateKey);
		PrivateKey privateKey = keyFactory.generatePrivate(privateKeySpec);
		return privateKey;
	}
	
	private static byte[] RSAEncrypt(byte[] bytesOriginal, PublicKey publicKey) 
			throws Exception, BadPaddingException {
		SecureRandom rand = new SecureRandom();
//		Cipher cipherEncrypt = Cipher.getInstance("RSA/NONE/OAEPPading"); //OAEPPading is typically used with RSA
		Cipher cipherEncrypt = Cipher.getInstance("RSA"); //OAEPPading is typically used with RSA
		cipherEncrypt.init(Cipher.ENCRYPT_MODE, publicKey, rand);
		byte[] bytesEncrypted = cipherEncrypt.doFinal(bytesOriginal);
		return bytesEncrypted;
	}
	
	private static byte[] RSADecrypt(byte[] bytesEncrypted, PrivateKey privateKey) 
			throws Exception, BadPaddingException {
//		Cipher cipherDecrypt = Cipher.getInstance("RSA/NONE/OAEPPading"); //OAEPPading is typically used with RSA
		Cipher cipherDecrypt = Cipher.getInstance("RSA"); //OAEPPading is typically used with RSA
		cipherDecrypt.init(Cipher.DECRYPT_MODE, privateKey);
		byte[] bytesDecrypted = cipherDecrypt.doFinal(bytesEncrypted);
		return bytesDecrypted;
	}
	
	private static void AESEncrypt(byte[] plainTextInBytes, byte[] cipherTextInBytes, 
			byte[] keyInBytes, byte[] ivInBytes) throws Exception {
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding"); 
//		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7Padding"); 
		
		Key key128AES = new SecretKeySpec(keyInBytes, "AES"); 	
		IvParameterSpec iv = new IvParameterSpec(ivInBytes); 
		
		cipher.init(Cipher.ENCRYPT_MODE, key128AES, iv);
		
		int nCipherLen = cipher.update(plainTextInBytes, 0, plainTextInBytes.length, cipherTextInBytes, 0);
		nCipherLen += cipher.doFinal(cipherTextInBytes, nCipherLen);
	}
	
	private static void AESDecrypt(byte[] decryptedTextInBytes, byte[] cipherTextInBytes, 
			byte[] keyInBytes, byte[] ivInBytes) throws Exception {
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding"); 
//		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7Padding"); 
		
		Key key128AES = new SecretKeySpec(keyInBytes, "AES"); 
		IvParameterSpec iv = new IvParameterSpec(ivInBytes); 
		
		cipher.init(Cipher.DECRYPT_MODE, key128AES, iv);
		int nDecryptedTextLen = cipher.update(
				cipherTextInBytes, 0, cipherTextInBytes.length,
				decryptedTextInBytes, 0);
		
		nDecryptedTextLen += cipher.doFinal(
				decryptedTextInBytes,
				nDecryptedTextLen);
	}
	
	private static byte[] signDigitalSignature(byte[] byteMessage, PrivateKey privateKey, String algorithm) 
			throws Exception {
		Signature sigSender = Signature.getInstance(algorithm);
		sigSender.initSign(privateKey);
		sigSender.update(byteMessage);
		byte[] bytesSignature = sigSender.sign();
		return bytesSignature;
	}
	
	private static boolean verifyDigitalSignature(byte[] byteMessage, byte[] byteSignature, 
			PublicKey publicKey, String algorithm) throws Exception {
		Signature sigReceiver = Signature.getInstance(algorithm);
		sigReceiver.initVerify(publicKey);
		sigReceiver.update(byteMessage);
		boolean bValid = sigReceiver.verify(byteSignature);
		return bValid;
	}
}
