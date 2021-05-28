import './App.css';
import {Component} from "react";

class App extends Component{
  constructor() {
    super();
    this.state = {
              WACC: 0,
              NOPAT: 0,
              EBI: 0,
              RV: 0,
              NCF: 0,
              ED: 0,
              CBI: 0,
              SVA: 0,
              CVA: 0,
              CFROI: 0,
              TSR: 0
    };
    this.calculateWACC = this.calculateWACC.bind(this);
    this.getWs = this.getWs.bind(this);
    this.getWd = this.getWd.bind(this);
    this.getKs = this.getKs.bind(this);
    this.getKd = this.getKd.bind(this);
    this.getT = this.getT.bind(this);
    this.getEBIT = this.getEBIT.bind(this);
    this.getNI = this.getNI.bind(this);
    this.getI = this.getI.bind(this);
    this.getGFA = this.getGFA.bind(this);
    this.getDEP = this.getDEP.bind(this);
    this.getN = this.getN.bind(this);
    this.getNA = this.getNA.bind(this);
    this.getCF = this.getCF.bind(this);
    this.getCI = this.getCI.bind(this);
    this.getQ0 = this.getQ0.bind(this);
    this.getP0 = this.getP0.bind(this);
    this.getQN = this.getQN.bind(this);
    this.getPN = this.getPN.bind(this);
    this.calculateRV = this.calculateRV.bind(this);
    this.calculateNCF = this.calculateNCF.bind(this);
    this.calculateED = this.calculateED.bind(this);
    this.calculateCBI = this.calculateCBI.bind(this);
    this.calculateSVA = this.calculateSVA.bind(this);
    this.calculateCVA = this.calculateCVA.bind(this);
    this.calculateCFROI = this.calculateCFROI.bind(this);
    this.calculateTSR = this.calculateTSR.bind(this);

  }

  calculateWACC(){
    fetch("http://localhost:5000/wacc", {
      method: 'POST',
      headers: new Headers(),
      body: JSON.stringify(this.state)
    }).then((res) => res.json())
        .then((data) => this.setState({WACC: data}))
        .catch((err) => console.log(err))
  }

  calculateRV(){
        fetch("http://localhost:5000/rv", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                RV: data.RV,
                WACC: data.WACC,
                EBI: data.EBI
            }))
            .catch((err) => console.log(err))
    }

    calculateNCF(){
        fetch("http://localhost:5000/ncf", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                NCF: data.NCF,
                EBI: data.EBI
            }))
            .catch((err) => console.log(err))
    }

    calculateED(){
        fetch("http://localhost:5000/ed", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                WACC: data.WACC,
                ED: data.ED
            }))
            .catch((err) => console.log(err))
    }

    calculateCBI(){
        fetch("http://localhost:5000/cbi", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                CBI: data.CBI,
                ED: data.ED,
                WACC: data.WACC,
                EBI: data.EBI
            }))
            .catch((err) => console.log(err))
    }

    calculateSVA(){
        fetch("http://localhost:5000/sva", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                NCF: data.NCF,
                WACC: data.WACC,
                EBI: data.EBI,
                RV: data.RV,
                SVA: data.SVA
            }))
            .catch((err) => console.log(err))
    }

    calculateCVA(){
        fetch("http://localhost:5000/cva", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                CBI: data.CBI,
                WACC: data.WACC,
                EBI: data.EBI,
                ED: data.ED,
                CVA: data.CVA
            }))
            .catch((err) => console.log(err))
    }

    calculateCFROI(){
        fetch("http://localhost:5000/cfroi", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                CFROI: data,
            }))
            .catch((err) => console.log(err))
    }

    calculateTSR(){
        fetch("http://localhost:5000/tsr", {
            method: 'POST',
            headers: new Headers(),
            body: JSON.stringify(this.state)
        }).then((res) => res.json())
            .then((data) => this.setState({
                TSR: data,
            }))
            .catch((err) => console.log(err))
    }

  getWs(event) {
    this.setState({Ws: event.target.value});
  }
  getWd(event) {
    this.setState({Wd: event.target.value});
  }
  getKs(event) {
    this.setState({Ks: event.target.value});
  }
  getKd(event) {
    this.setState({Kd: event.target.value});
  }
  getT(event) {
    this.setState({T: event.target.value});
  }
  getEBIT(event){
    this.setState({EBIT: event.target.value})
  }
  getNI(event){
    this.setState({NI: event.target.value})
  }
  getI(event){
    this.setState({I: event.target.value})
  }
  getGFA(event){
    this.setState({GFA: event.target.value})
  }
  getDEP(event){
    this.setState({DEP: event.target.value})
  }
  getN(event){
    this.setState({N: event.target.value})
  }
  getNA(event){
    this.setState({NA: event.target.value})
  }
  getCF(event){
    this.setState({CF: event.target.value})
  }
  getCI(event){
    this.setState({CI: event.target.value})
  }
  getQ0(event){
    this.setState({Q0: event.target.value})
  }
  getP0(event){
    this.setState({P0: event.target.value})
  }
  getQN(event){
    this.setState({QN: event.target.value})
  }
  getPN(event){
    this.setState({PN: event.target.value})
  }
  render() {
    return (
        <div className="col">
            <div className='row-3'>
                <label>
                    Удельный вес собственного капитала:
                     <input type="number" id="inputWACC1" className="form-control"
                            placeholder="Удельный вес собственного капитала"
                     onChange={this.getWs}/>
                </label>
            </div>
            <div className='row'>
                <label>
                    Удельный вес заемного капитала:
                 <input type="number" className="form-control" placeholder="Удельный вес заемного капитала" onChange={this.getWd}/>
                </label>
            </div>
            <div className='row'>
                <label>
                    Стоимость собственного капитала:
                 <input type="number" className="form-control" placeholder="Стоимость собственного капитала" onChange={this.getKs}/>
                </label>
            </div>
            <div className='row'>
                <label>
                    Стоимость заемного капитала:
                 <input type="number" className="form-control" placeholder="Стоимость заемного капитала" onChange={this.getKd}/>
                </label>
            </div>
            <div className='row'>
                <label>
                    Налог на прибыль:
                    <input type="text" className="form-control" placeholder="Налог на прибыль"  onChange={this.getT}/>
                </label>
            </div>
           <p/>

          <div className="row">
             <input type="text" className="form-control" placeholder="Показатель операционной прибыли до вычета налогов"
                    aria-label="Показатель операционной прибыли до вычета налогов" onChange={this.getEBIT}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Чистая прибыль" aria-label="Чистая прибыль" onChange={this.getNI}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Процентные расходы" aria-label="Процентные расходы" onChange={this.getI}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Внеоборотные активы" aria-label="Внеоборотные активы" onChange={this.getGFA}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Бухгалтерская амортизация" aria-label="Бухгалтерская амортизация" onChange={this.getDEP}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Период" aria-label="Период" onChange={this.getN}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Чистые активы" aria-label="Чистые активы" onChange={this.getNA}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Денежные притоки" aria-label="Денежные притоки" onChange={this.getCF}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Денежные инвестиции" aria-label="Денежные инвестиции" onChange={this.getCI}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Первоначальное количество акций"
                    aria-label="Первоначальное количество акций" onChange={this.getQ0}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Первоначальная стоимость акций"
                    aria-label="Первоначальная стоимость акций" onChange={this.getP0}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Текущая стоимость акций" aria-label="Текущая стоимость акций" onChange={this.getPN}/>
           </div>
           <div className="col">
             <input type="text" className="form-control" placeholder="Текущее количество акций" aria-label="Текущее количество акций" onChange={this.getQN}/>
           </div>
            <p/>
            <div className='row'>
            <input className="form-uncontrol" type="number" placeholder="Значение WACC" value={this.state.WACC}
                   aria-label="Disabled input example" disabled/>

            <div className='button__container'>
                <button className='button' onClick={this.calculateWACC}>
                    Рассчитать WACC
                </button>
                <div className="col">
                    <input className="form-uncontrol" type="text" placeholder="Значение NOPAT" value={this.state.NOPAT}
                           aria-label="Disabled input example" disabled/>
                </div>
            </div>
           <div className="col">
             <button type="button" className="btn btn-primary">Рассчитать NOPAT</button>
           </div>
            </div>
             <div className="col">
               <input className="form-uncontrol" type="text" placeholder="Значение EBI" aria-label="Disabled input example" value={this.state.EBI}
                      disabled/>
             </div>
            <div className="col">
                <button type="button" className="btn btn-primary">Рассчитать EBI</button>
            </div>
             <div className="col">
               <input className="form-uncontrol" type="text" placeholder="Значение RV" aria-label="Disabled input example" value={this.state.RV}
                      disabled/>
             </div>
             <div className="col">
               <button type="button" className="btn btn-primary" onClick={this.calculateRV}>Рассчитать RV</button>
             </div>
             <div className="col">
               <input className="form-uncontrol" type="text" placeholder="Значение NCF" aria-label="Disabled input example" value={this.state.NCF}
                      disabled/>
             </div>
             <div className="col">
               <button type="button" className="btn btn-primary" onClick={this.calculateNCF}>Рассчитать NCF</button>
             </div>
             <div className="col">
               <input className="form-uncontrol" type="text" placeholder="Значение ED" aria-label="Disabled input example" value={this.state.ED}
                      disabled/>
             </div>
             <div className="col">
               <button type="button" className="btn btn-primary" onClick={this.calculateED}>Рассчитать ED</button>
             </div>
             <div className="col">
               <input className="form-uncontrol" type="text" placeholder="Значение CBI" aria-label="Disabled input example" value={this.state.CBI}
                      disabled/>
             </div>
             <div className="col">
               <button type="button" className="btn btn-primary" onClick={this.calculateCBI}>Рассчитать CBI</button>
             </div>
               <div className="col">
                 <input className="form-uncontrol" type="text" placeholder="Значение SVA" value={this.state.SVA}
                        aria-label="Disabled input example" disabled/>
               </div>
               <div className="col">
                 <button type="button" className="btn btn-primary" onClick={this.calculateSVA}>Рассчитать SVA</button>
               </div>
               <div className="col">
                 <input className="form-uncontrol" type="text" placeholder="Значение CVA" value={this.state.CVA}
                        aria-label="Disabled input example" disabled/>
               </div>
               <div className="col">
                 <button type="button" className="btn btn-primary" onClick={this.calculateCVA}>Рассчитать CVA</button>
               </div>
               <div className="col">
                 <input className="form-uncontrol" type="text" placeholder="Значение CFROI" value={this.state.CFROI}
                        aria-label="Disabled input example" disabled/>
               </div>
               <div className="col">
                 <button type="button" className="btn btn-primary" onClick={this.calculateCFROI}>Рассчитать CFROI</button>
               </div>
               <div className="col">
                 <input className="form-uncontrol" type="text" placeholder="Значение TSR" value={this.state.TSR}
                        aria-label="Disabled input example" disabled/>
               </div>
               <div className="col">
                 <button type="button" className="btn btn-primary" onClick={this.calculateTSR}>Рассчитать TSR</button>
               </div>
        </div>
    )
  }
  }


export default App;
