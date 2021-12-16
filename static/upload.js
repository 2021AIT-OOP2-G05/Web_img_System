
// img要素を作成
var img_element = document.createElement('img');
img_element.src = 'image/01.png'; // 画像パス
img_element.alt = 'さいくん'; // 代替テキスト
img_element.width = 200; // 横サイズ（px）
img_element.height = 200; // 縦サイズ（px）

// 指定した要素にimg要素を挿入
var content_area = document.getElementById("imglist");
content_area.appendChild(img_element);