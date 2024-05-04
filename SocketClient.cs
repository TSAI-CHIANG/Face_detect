using UnityEngine;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Collections;
using System.Collections.Generic;

public class SocketClient : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private string serverIP = "127.0.0.1";
    private int serverPort = 12345;

    void Start()
    {
        ConnectToServer();
    }

    void ConnectToServer()
    {
        try
        {
            client = new TcpClient(serverIP, serverPort);
            stream = client.GetStream();
            Debug.Log("Connected to server!");

            // Start a new thread to receive data from the server
            Thread receiveThread = new Thread(new ThreadStart(ReceiveData));
            receiveThread.IsBackground = true;
            receiveThread.Start();
        }
        catch (SocketException e)
        {
            Debug.LogError("Socket exception: " + e.ToString());
        }
    }

    void ReceiveData()
    {
        byte[] bytes = new byte[1024];
        while (client.Connected)
        {
            if (stream.CanRead)
            {
                int length = stream.Read(bytes, 0, bytes.Length);
                if (length > 0)
                {
                    string data = Encoding.ASCII.GetString(bytes, 0, length);
                    Debug.Log("Received data: " + data);
                    // Process data
                }
            }
        }
    }

    void OnApplicationQuit()
    {
        if (stream != null) stream.Close();
        if (client != null) client.Close();
    }
}




// using System.Collections;
// using System.Collections.Generic;
// using UnityEngine;

// public class SocketClient : MonoBehaviour
// {
//     // Start is called before the first frame update
//     void Start()
//     {
        
//     }

//     // Update is called once per frame
//     void Update()
//     {
        
//     }
// }
