const Main = () => {
    return (
        <div align="center">
            {'Enjoy the analysis!'}
        </div>
    );
};

const domContainer = document.querySelector('#stock_form');
ReactDOM.render(<Main />, domContainer);
