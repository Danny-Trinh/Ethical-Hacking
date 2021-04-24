import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div classNameName="App">
      <h1 style={{ textAlign: "center" }}>
        The blog that is definitely a real blog
      </h1>
      <div className="container marketing ">
        <div className="row">
          <div className="col-lg-4">
            <img
              className="bd-placeholder-img rounded-circle"
              width="140"
              height="140"
              alt="danny pic"
              src="https://i.pinimg.com/474x/99/97/9e/99979e5146ad57a12a11d3ff3d195aac.jpg"
            ></img>
            <h2>Danny Trinh</h2>
            <p>My email is trinh644@gmail.com</p>
            <p>
              <button className="btn btn-secondary">View details »</button>
            </p>
          </div>
          <div className="col-lg-4">
            <img
              className="bd-placeholder-img rounded-circle"
              width="140"
              height="140"
              alt="regina pic"
              src="https://www.goldfishfun.com/wp-content/uploads/2018/06/gff-swimmington.png"
            ></img>
            <h2>Charles Cao</h2>
            <p>My email is doomseeker12345@gmail.com</p>
            <p>
              <button className="btn btn-secondary">View details »</button>
            </p>
          </div>
          <div className="col-lg-4">
            <img
              className="bd-placeholder-img rounded-circle"
              width="140"
              height="140"
              alt="regina pic"
              src="https://www.goldfishfun.com/wp-content/uploads/2018/06/gff-brooke.png"
            ></img>
            <h2>Regina Chen</h2>
            <p>My email is regthephish@gmail.com</p>
            <p>
              <button className="btn btn-secondary">View details »</button>
            </p>
          </div>
          <div className="col-lg-4">
            <img
              className="bd-placeholder-img rounded-circle"
              width="140"
              height="140"
              alt="mitchell pic"
              src="https://i.guim.co.uk/img/media/c26ced2bb6cbf1e770623712c0b02e1a5b024edd/0_0_4728_2837/master/4728.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=697e097424a84242cb3fc787a77d38b5"
            ></img>
            <h2>Mitchell Watkins</h2>
            <p>My email is mawatkins99@yahoo.com</p>
            <p>
              <button className="btn btn-secondary">View details »</button>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
