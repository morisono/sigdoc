const inputField = document.querySelector('#quiz-answer');
const submitButton = document.querySelector('#submit-quiz-answer');
const regexPattern = '[ア-ン]{3}';
const firstChar = 'ア';
const lastChar = 'ン';
const length = 3;


// 辞書生成関数
function generateDictionary(length) {
  let strings = [];
  const charCodeFirst = firstChar.charCodeAt(0);
  const charCodeLast = lastChar.charCodeAt(0);

  // 指定された長さの文字列を生成
  function generateString(currentStr, depth) {
    if (depth === length) {
      if (currentStr.match(new RegExp(regexPattern))) {
        strings.push(currentStr);
      }
      return;
    }

    for (let i = charCodeFirst; i <= charCodeLast; i++) {
      generateString(currentStr + String.fromCharCode(i), depth + 1);
    }
  }

  // 初期文字列から開始して、長さを満たす文字列を生成
  for (let i = charCodeFirst; i <= charCodeLast; i++) {
    generateString(String.fromCharCode(i), 1);
  }

  console.log('Done generating dictionary');
  return strings;
}

const strings = generateDictionary(length);


let counter = 1;
async function inputAndClick() {
  inputField.value = '';
  inputField.value = strings[counter]; //TODO
  submitButton.click();
  counter++;
  setTimeout(inputAndClick, 100);
}

window.addEventListener('load', () => {
  setTimeout(inputAndClick, 100);
});