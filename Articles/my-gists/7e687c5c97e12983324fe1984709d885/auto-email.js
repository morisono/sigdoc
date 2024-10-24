// 入力フィールドと確認ボタンの要素を取得
const inputField = document.querySelector('#quiz-answer');
const submitButton = document.querySelector('#submit-quiz-answer');

// カウンターの初期値を設定
let counter = 1;

// ページ遷移を検出するフラグ
let isPageNavigated = false;

// Emailアドレスのパターンを表す正規表現
const emailPattern = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

// ランダムな文字列を生成する関数
function generateRandomString(length) {
  let result = '';
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!#$%&\'*+/=?^_`{|}~-@';
  const charactersLength = characters.length;
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

// 入力と確認ボタンのクリックを行う関数
async function inputAndClick() {
  // テキストフォームが見つからない場合は処理を中断
  if (!inputField || !submitButton) {
    console.log('テキストフォームが見つからないため、処理を中断しました。');
    return;
  }

  // ページ遷移が検出された場合は処理を中断
  if (isPageNavigated) {
    console.log('ページ遷移が検出されたため、処理を中断しました。');
    return;
  }

  // 入力フィールドを空にする
  inputField.value = '';

  // ランダムな文字列を生成し、Emailアドレスのパターンに合致するまで試行する
  let randomString;
  do {
    randomString = generateRandomString(15); // 15文字のランダム文字列を生成
  } while (!emailPattern.test(randomString)); // Emailアドレスのパターンに合致しない場合は再試行

  // 入力フィールドにランダムな文字列を設定
  inputField.value = randomString;

  // 確認ボタンをクリック
  submitButton.click();

  // カウンターをインクリメント
  counter++;

  // カウンターが1001になったら終了
  if (counter === 1001) {
    console.log('終了しました。');
    return;
  }

  // 次の入力とクリックを行う
  setTimeout(inputAndClick, 100);
}

// ページ遷移を検出するイベントリスナー
window.addEventListener('beforeunload', () => {
  isPageNavigated = true;
});

// 処理を遅延して開始
window.addEventListener('load', () => {
  setTimeout(inputAndClick, 100);
});