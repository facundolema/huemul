import fs from "fs";
import path from "path";

export default {
  paths() {
    return readdirrec("./content", new Array());
  },
};

function readdirrec(dir, list) {
  fs.readdirSync(dir).map((file) => {
    if (fs.statSync(path.join(dir, file)).isDirectory()) {
      readdirrec(path.join(dir, file), list);
    }
    list.push({ params: { id: file } });
  });
  return list;
}
