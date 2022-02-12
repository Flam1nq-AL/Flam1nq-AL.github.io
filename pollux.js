const morse2char = {
  ".-": "a",
  "-...": "b",
  "-.-.": "c",
  "-..": "d",
  ".": "e",
  "..-.": "f",
  "--.": "g",
  "....": "h",
  "..": "i",
  ".---": "j",
  "-.-": "k",
  ".-..": "l",
  "--": "m",
  "-.": "n",
  "---": "o",
  ".--.": "p",
  "--.-": "q",
  ".-.": "r",
  "...": "s",
  "-": "t",
  "..-": "u",
  "...-": "v",
  ".--": "w",
  "-..-": "x",
  "-.--": "y",
  "--..": "z",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
  "-----": "0",
  "..--.-": "_",
  "-....-": "-",
  "--..--": ",",
  "-.-.-.": ";",
  "---...": ":",
  "..--..": "?",
  ".-.-.-": ".",
  ".----.": "'",
  ".-..-.": '"',
  "-.--.": "(",
  "-.--.-": ")",
  "-..-.": "/",
  ".-.-.": "+",
  "-...-": "=",
  "...-..-": "$",
  " ": " ",
  "": " ",
};
/* eslint-enable sort-keys */

// DCODEPOLLUX
// const ciphertext = '1709434021559587989345091149340868137288495381';
// badge text
const ciphertext =
  "6WINFVHJU2ONTIA2P256WLHP5845RDQD89HP5CFNRFYVCOVP6WVXONUPOF89HPPVOVVJVP3PEYAWPWY8RDNPE5CPAVFN75W6AWBYJR2U4B56VZVO";

const test = (lookup) => {
  let morse = [...ciphertext].map((x) => lookup[x]);
  morse = morse.join("");
  morse = morse.split(" ").filter((x) => x !== "");

  morse = morse.map((x) => morse2char[x]);

  if (morse.some((x) => x === undefined)) return false;

  morse = morse.join("");
  return morse;
};

const morseSymbols = ["-", ".", " "];
const cipherSymbols = Object.keys(
  [...ciphertext].reduce((s, x) => {
    s[x] = true;

    return s;
  }, {})
);

let results = [];
for (let i = 0; i < morseSymbols.length ** cipherSymbols.length; i++) {
  const lookup = cipherSymbols.reduce((s, x, j) => {
    s[x] =
      morseSymbols[
        Math.floor(i / morseSymbols.length ** j) % morseSymbols.length
      ];

    return s;
  }, {});

  const ret = test(lookup);
  if (ret) results.push(ret);
}

// remove any duplicate entries
results = Object.keys(
  results.reduce((s, x) => {
    s[x] = true;

    return s;
  }, {})
);

console.log(`Found ${results.length} potential solutions:`);
results.forEach((x) => {
  console.log(x);
});
