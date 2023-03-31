import processing.serial.*;
Serial port;
float[] data = new float[1];


void setup()
{
  size(300,300);
  port = new Serial(this, "COM1", 9600);//crea e puerto 9600 debe ser igaul en Arduino
  port.bufferUntil('\n');
}

void draw()
{
  for(int a=0; a<=310; a= a+10){
    textSize(15);    
    text("CERCA", 50, 30); 
    text("LEJOS", 200, 30); 
    strokeWeight(1);
    stroke(#FFFFFF);
    line(150,0,150,300);
    stroke(0);
    strokeWeight(10);
    line(0, a, 800, a);
    stroke(a, 20, 40);
    line(data[0]*9,a,800,a);
  }
}

void serialEvent(Serial port) {
  String bufString = port.readString();
  data = float(split(bufString, ','));
}
