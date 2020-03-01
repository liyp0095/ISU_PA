import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;

public class AsymmetricKeyProducer {
	
	public static void main(String[] args) throws NoSuchAlgorithmException, IOException {
		
//		String privateKeyFile = "client.key";
//		String publicKeyFile = "client.key.pub";
		//String privateKeyFile = "server.key";
		//String publicKeyFile = "server.key.pub";

		if (args.length < 2) {
			System.out.println("Not enough arguments \nUsage: java AsymmetricKeyProducer [public key file] [pricate key file]");
			return;
		}

		String privateKeyFile = args[1];
		String publicKeyFile = args[0];
		String algorithm = "RSA";
		
		KeyPair kp = generateKeyPair(algorithm);
		storePublicKey(kp.getPublic(), publicKeyFile);
		storePrivateKey(kp.getPrivate(), privateKeyFile);
	}
	
	private static KeyPair generateKeyPair(String algorithm) throws NoSuchAlgorithmException {
		SecureRandom rand = new SecureRandom();
		KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
		
		kpg.initialize(2048, rand);

		return kpg.generateKeyPair();
	}
	
	private static void storePrivateKey(PrivateKey privateKey, String path) throws IOException {
		PKCS8EncodedKeySpec pkcs8EncodedKeySpec = new PKCS8EncodedKeySpec(privateKey.getEncoded());
		FileOutputStream fos = new FileOutputStream(path);
		fos.write(pkcs8EncodedKeySpec.getEncoded());
		fos.close();
	}
	
	private static void storePublicKey(PublicKey publicKey, String path) throws IOException {
		X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(publicKey.getEncoded());
		FileOutputStream fos = new FileOutputStream(path);
		fos.write(x509EncodedKeySpec.getEncoded());
		fos.close();
	}
}
