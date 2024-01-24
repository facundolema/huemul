import fs from "fs";
import path from "path";

export const generateSidebar = (folder) => {
  return fs.readdirSync(folder).map((subfolder) => {
    const link = path.join(folder, subfolder);
    const text =
      subfolder[0].toUpperCase() + subfolder.slice(1).replace(/_/g, " ");
    const item = { text: text, link: subfolder, collapsed: true };

    return fs.statSync(folder).isDirectory()
      ? { ...item, items: generateSidebar(link) }
      : item;
  });
};
