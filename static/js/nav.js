function Application() {
  return (
    <nav className="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div className="container">
            <div className="navbar-header">
                <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span className="sr-only">Toggle navigation</span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                    <span className="icon-bar"></span>
                </button>
                <a className="navbar-brand" href="/">Greek Mythology</a>
            </div>
            <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul className="nav navbar-nav">
                    <li>
                        <a href="/static/gods.html">Gods</a>
                    </li>
                    <li>
                        <a href="/static/heroes.html">Heroes</a>
                    </li>
                    <li>
                        <a href="/static/creatures.html">Creatures</a>
                    </li>
                    <li>
                        <a href="/static/myths.html">Myths</a>
                    </li>
                    <li>
                        <a href="/static/about.html">About</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
  );
}

ReactDOM.render(<Application/>, document.getElementById('nav'));
