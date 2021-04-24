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
              src="https://miro.medium.com/max/1800/1*DNs5M8noio5r3_E6DB5Mfg.jpeg"
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
              src="https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png"
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
              src="https://upload.wikimedia.org/wikipedia/en/7/78/Bilbo_Baggins.jpg"
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
            <p>My email is regthephish@gmail.com</p>
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
