import React from "react";
import "./estilo.css";
import api from '../../api'


function FormularioCalculo(){
  const [data, setData] = React.useState({
    
  });
  
  async function submit (e){
      e.preventDefault();
      const {Salario,Desconto,Dependente} = e.target
      console.log(Salario.value)
      const dados ={
        salarioBruto: Salario.value,
        desconto: Desconto.value,
        dependente: Dependente.value
      }
      console.log("formulario",dados)

      try {
        const  res = await api.post('/calcular',dados)
        console.log("apiRes",res)
        setData(res.data)  
      } catch(error){
          console.log(error)
      }   
  }   
  
    return (
      <form className="form-cadastro"
        onSubmit={submit}
      >
        <input type="text" placeholder="Salario" name="Salario" className="form-cadastro_input"
          
        />
        <input type="text" placeholder="Desconto" name="Desconto" className="form-cadastro_input"
          
        />
        <input type="text" placeholder="Dependente" name="Dependente" className="form-cadastro_input"
          
        />
        <button type="submit" className="form-cadastro_input form-cadastro_submit">
          Calcular
        </button>
      </form>
    );
  
}
export default FormularioCalculo;
