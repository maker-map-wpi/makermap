import React from "react";
import  {BrowserRouter as Router,Switch,Route} from 'react-router-dom'

import Navbar from './components/Navbar'
import Map from './components/Map'

export default () => (
  <Router>
    <Navbar>
    <Switch>
    <Route path="/">
      <Map />
    </Route>

    </Switch>
    </Navbar>
  </Router>

);
