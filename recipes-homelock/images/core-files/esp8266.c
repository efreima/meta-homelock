#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Arduino_JSON.h>
#include <ESP8266HTTPClient.h>
#define LOGGING

const char* ssid = "HomeLock";         
const char* password = "homelock";

const char* serverName = "http://192.168.1.2:80/statuses.json";

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 500;

String sensorReadings;
//bool sensorReadingsArr[1];
int sensorReadingsArr[1];

ESP8266WebServer server(80);   //instantiate server at port 80 (http port)

String page = ""; //For the Web Server
String page2="";  //For updating Status of motor 1
String page3="";  //For updating status of motor 2


bool hasLockRun = false;

void setup(void)
{
  bool isLocked = NULL;  
  
  //the HTML of the web page
  page = "<center><h1>Motor Control Web Server</h1><body><p><a href=\"Forward\"><button>Lock</button></a><p><a href=\"Backward\"><button>Unlock</button></a></p><p><a href =\"Left\"><button>Left</button></a>&nbsp;<a href=\"Stop\"><button>Stop</button></a><a href=\"Right\"><button>Right</button></a></p></body></center>";
  pinMode(D5, OUTPUT);   // inputs for motor 1
  pinMode(D6,OUTPUT);
  pinMode(D7,OUTPUT);    // inputs for motor 2 
  pinMode(D8,OUTPUT);
  pinMode(LED_BUILTIN,OUTPUT);  // For status of WiFi connection
  delay(1000);
  Serial.begin(115200);     
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  digitalWrite(LED_BUILTIN,HIGH);     // when connected turns high
  Serial.println("");
  Serial.print("Connected to ");   
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());   //provides IP address
   server.on("/", [](){
    server.send(200, "text/html", page+page2);
  });
  server.on("/Forward",Forward);
  server.on("/Backward",Backward);
  server.on("/Left",Left);
  server.on("/Right",Right);

  server.on("/Stop",[](){                              // turns all the motor input pins low
   page2="<center><p> motor 1 Status : Off</p></center>";
   page3="<center><p> motor 2 Status : off</p></center>";
  server.send(200,"text/html",page+page2+page3);
    digitalWrite(D5,LOW);
    digitalWrite(D6,LOW);
    digitalWrite(D7,LOW);
    digitalWrite(D8,LOW);
    delay(200);
  });
  server.begin();
  Serial.println("Web server started!");
}
void loop(void)
{  
     // Send an HTTP POST request depending on timerDelay
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
              
      sensorReadings = httpGETRequest(serverName);
      Serial.println(sensorReadings);
      JSONVar myObject = JSON.parse(sensorReadings);
  
      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (JSON.typeof(myObject) == "undefined") {
        Serial.println("Parsing input failed!");
        return;
      }
    
      Serial.print("JSON object = ");
      Serial.println(myObject);
    
      // myObject.keys() can be used to get an array of all the keys in the object
      JSONVar keys = myObject.keys();
    
      for (int i = 0; i < keys.length(); i++) {
        JSONVar value = myObject[keys[i]];
        Serial.print(keys[i]);
        Serial.print(" = ");
        Serial.println(value);
        sensorReadingsArr[i] = double(value);
        Serial.print("key = ");
        Serial.println(i);

        if (sensorReadingsArr[0] == true && hasLockRun == false){
          Serial.println("Executing lock"); 
          Forward();
          hasLockRun = true;
        }

        if (sensorReadingsArr[0] == false && hasLockRun == true){
          Serial.println("Executing unlock");
          Backward();
          hasLockRun = false;  
        }
        
      }
      
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
  
     server.handleClient();
}

String httpGETRequest(const char* serverName) {
  WiFiClient client;
  HTTPClient http;
    
  // Your IP address with path or Domain name with URL path 
  http.begin(client, serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
 }

 void Forward() 
 {
    digitalWrite(D5,HIGH);
    delay(3000);
    digitalWrite(D5, LOW);

//    isLocked = true;
    
    digitalWrite(D6,LOW);
    page2="<center><p> motor 1 Status : Forward </p></center>";
    server.send(200,"text/html", page+page2+page3);
    delay(200);
  }
  void Left()
  {
    page3="<center><p> motor 2 Status : Left</p></center>";
    server.send(200,"text/html",page+page2+page3);
    digitalWrite(D7,HIGH);
    digitalWrite(D8,LOW);
    delay(200);
  }
  void Right()
   { 
    page3="<center><p> motor 2 Status : Right</p></center>";
    server.send(200,"text/html",page+page2+page3);
    digitalWrite(D8,HIGH);
    digitalWrite(D7,LOW);
    delay(200);
  }
   void Backward()
  {
    page2="<center><p> motor 1 Status : Backward</p></center>";
    server.send(200, "text/html", page+page2+page3);
    digitalWrite(D6, HIGH);
    delay(3300);
    digitalWrite(D6, LOW);
    digitalWrite(D5,LOW);
    delay(200); 
  }
