var Main = function Main() {
    return React.createElement(
        'div',
        { align: 'center' },
        'Enjoy the analysis!'
    );
};

var domContainer = document.querySelector('#stock_form');
ReactDOM.render(React.createElement(Main, null), domContainer);