const inputField = document.querySelector('#quiz-answer');
const submitButton = document.querySelector('#submit-quiz-answer');
const regexPattern = '[ぁ-んァ-ン]{3}';
const firstChar = 'ぁ';
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

// 提出関数
let counter = 0;
function submitString() {
  inputField.value = strings[counter];
  submitButton.click();
  counter++;

  if (counter === strings.length) {
    clearInterval(interval);
    console.log('Done submitting');
  }
}

// 最初の提出を手動で実行
submitButton.addEventListener('click', function firstSubmission() {
  submitString();
  submitButton.removeEventListener('click', firstSubmission);
});

// レスポンスを受け取った後、次の文字列を提出
submitButton.addEventListener('click', function handleResponse() {
  submitString();
});

// インターバル
const interval = setInterval(() => {
  // レスポンスが返ってくる前に提出を行う
  if (counter === 0) {
    return;
  }
  
  submitString();
}, 1); // 1秒ごとに提出
