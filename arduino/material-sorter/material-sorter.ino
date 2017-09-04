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

#define BELT_LEN 3
#define BIN_CNT 1
#define BIN_OFF BELT_LEN - BIN_CNT

struct Material bins[BIN_CNT] {
  {MaterialType::Bolt, 1, 3.0/8.0}
};

struct Material belt[BELT_LEN];

void setup() {

}

void loop() {

}
