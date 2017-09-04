enum MaterialType {
  Bolt,
  Screw,
  Nut,
  Washer,
  Other
};

struct Material {
  enum MaterialType type;
  double length;
  double width; //aka inner diameter
};

struct Material materials[] {
  {MaterialType::Bolt, 1, 3.0/8.0}
};

void setup() {

}

void loop() {

}
