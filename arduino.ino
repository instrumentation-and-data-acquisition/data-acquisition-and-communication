
int val = 0; //variavel onde se guarda valor de tensao de porta analogica
int analogPin = A0;  //porta analogica escolhida
void setup() {
  Serial.begin(9600); //baut rate de 9600 bits por segundo
}
void loop() {
  if (Serial.available() > 0) {       //retorna o numero de caracteres disponiveis para leitura na porta serial
    String data = Serial.readString(); //guarda na string data a string recebida pelo Raspberry Pi
  if(data.equalsIgnoreCase("start")){  //compara a string data ao comando correto pretendido - "start".
    val = analogRead(analogPin);       //caso o comando seja correto lê o valor da porta analógica 
    Serial.print(val);                // e manda ao Raspberry Pi
    Serial.flush();                  //o flush garante que todos os dados foram transmitidos antes de prosseguir com o programa
  }
  else{
   Serial.print("FATAL ERROR");    // se o comando lido do Raspberry nao for o correto, o Arduino envia a mensagem "FATAL ERROR"
   Serial.flush();
  }
  }
}
