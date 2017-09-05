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
  bool operator==(const Material& other) {
    return this->type == other.type && this->length == other.length && this->width == other.width;
  }
};