import React, { Component } from "react";
import FormularioCalculo from "./components/FormularioCalculo";
import "./assets/App.css";
import './assets/index.css';
class App extends Component {

  render() {
    return (
      <section className="conteudo">
        <FormularioCalculo />
      </section>
    );
  }
}

//new ListaDeNotas({notas:this.notas})
export default App;
