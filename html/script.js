/**
 * イベントリスナーの追記
 */
// 入力した文字列を検索する
const search = document.getElementById("search");
search.addEventListener('click', () => {
    const input_text = document.getElementById("input_text").value;
    const source_file = document.getElementById("source_file").value;
    // 課題2 検索ワード入力が空の場合アラートを表示
    if (!input_text) window.alert("検索文字を入力してください。")
    if (!source_file) window.alert("保存先を入力してください。")

    eel.kimetsu_search(input_text, source_file)
});

// 保存先を選択する
const save_file = document.getElementById("source_select")
save_file.addEventListener('click', async() => {
    const file = await eel.select_save_file()();
    document.getElementById("source_file").value = file
})

/**
 * pythonに渡す関数
 */

eel.expose(view_log_js)
function view_log_js(text){
    // 課題4 ログにkimetsu_searchの結果を表示
    document.getElementById("log_area").value += text + "\n";
}