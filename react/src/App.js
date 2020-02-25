import React from "react";
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

import Navbar from './components/Navbar'
import Map from './components/Map'

export default class App extends React.Component {
  constructor() {
    super()
    this.state = {
      'sidebar': true,
      'data':[]
    }
    this.handleClick=this.handleClick.bind(this)

  }

  async componentDidMount(){
    const response= await fetch('https://api.makermap-wpi.com/searchMap')
    const data= await response.json();

    this.setState({
      'data': JSON.parse(data.body)
    })
    console.log(JSON.parse(data.body))
  }

  handleClick() {
    this.setState({
      'sidebar': !this.state.sidebar
    })
  }

  render() {
    return <Router>
      <Navbar click={this.state.sidebar}>
        <Switch>
          <Route path="/">
            <Map data= {this.state.data} click={this.handleClick}/>
          </Route>

        </Switch>
      </Navbar>
    </Router>
  }
};
