import java.io.*;
import java.net.*;
import java.nio.file.Files;
import java.nio.file.Paths;
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

public class Server {
//	a. The Server’s port number;
//	b. A file containing the server’s private key;
//	c. A file containing the client’s public key; and
//	d. A text file.
	
	public static void main(String[] args) throws Exception {
		String serverIP = "127.0.0.1";
		String serverPrivateKeyFile = "server.key";
		String clientPublicKeyFile = "client.key.pub";
		String textFile = "text.txt";
		
		PrivateKey serverPrivateKey = loadPrivateKey(serverPrivateKeyFile, "RSA");
		PublicKey clientPublicKey = loadPublicKey(clientPublicKeyFile, "RSA");
		
		byte[] plainTextInBytes = loadTextFile(textFile);
		
		ServerSocket serverSocket = new ServerSocket(6789);
		
		while (true) {
		   Socket encryptSocket = serverSocket.accept();
//		   BufferedReader inFromClient = new BufferedReader(
//				   new InputStreamReader(encryptSocket.getInputStream()));
		   DataOutputStream outToClient = new DataOutputStream(encryptSocket.getOutputStream());
		   DataInputStream inFromClient = new DataInputStream(encryptSocket.getInputStream());
		   
		   // receiving 
		   int ciphertextLength = inFromClient.readInt();
		   byte[] RSAEncryptedKey128K = new byte[ciphertextLength];
		   inFromClient.readFully(RSAEncryptedKey128K);
		   
		   int signatureLength = inFromClient.readInt();
		   byte[] signatureKey128K = new byte[signatureLength];
		   inFromClient.readFully(signatureKey128K);
		   
		   // decryption and verification
		   byte[] key128K = RSADecrypt(RSAEncryptedKey128K, serverPrivateKey);
		   boolean valid = verifyDigitalSignature(key128K, signatureKey128K, clientPublicKey, "SHA512withRSA");
		   
		   if (!valid) {
			   System.err.println("verification error!");
			   continue;
		   }
		   
		   // AES encryption 
		   SecureRandom sr = new SecureRandom();
		   byte[] ivInBytes = new byte[16];
		   sr.nextBytes(ivInBytes);
		   byte[] cipherTextInBytes = new byte[(plainTextInBytes.length / 16) * 16 + 16];
//		   System.out.println(plainTextInBytes.length);
		   AESEncrypt(plainTextInBytes, cipherTextInBytes, key128K, ivInBytes);
		   
		   // send cipher text and IV to client
		   outToClient.writeInt(cipherTextInBytes.length);
		   outToClient.write(cipherTextInBytes);
		   outToClient.writeInt(ivInBytes.length);
		   outToClient.write(ivInBytes);
		   
		   
//		   System.out.println("Received: " + new String(key128K));
//		   System.out.println("Received: " + valid);
////		   System.out.println("Received: " + new String(signatureKey128K));
////		   capitalizedSentence = clientSentence.toUpperCase() + '\n';
////		   outToClient.writeBytes(capitalizedSentence);
		}
	}
	
	private static byte[] loadTextFile(String textFile) throws IOException {
		byte[] b = Files.readAllBytes(Paths.get(textFile));
		return b;
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
