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

//how many sections are on the belt, starting at the image sensor, ending at the end of the belt
#define BELT_LEN 3
//how many storage bins there are for different material types
#define BIN_CNT 1
//offset between image sensor and first storage bin
#define BIN_OFF BELT_LEN - BIN_CNT
//offset for DIO pins for the bin kickers - i.e. bin 2's kicker is on DIO 2+BIN_DIO
#define BIN_DIO 3

struct Material bins[BIN_CNT] {
  {MaterialType::Bolt, 1, 3.0/8.0}
};

struct Material belt[BELT_LEN];

void setup() {
  //TODO serial communication init
  //TODO verify connection with Pi
}

void loop() {
  rotateBelt(1);
  addMaterial(getImageMaterial());
  pushMaterials();
  delay(100);
}

void rotateBelt(int counts) {
  //TODO rotate belt
}

struct Material getImageMaterial() {
  //TODO get material data from Pi
}

void addMaterial(struct Material material) {
  //TODO shift stack, add new
}

void pushMaterials() {
  //TODO check each material, push if necessary
}

void pushBin(int number) {
  //TODO push that bin kicker
}

