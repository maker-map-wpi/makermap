import React from "react";
import  {BrowserRouter as Router,Switch,Route} from 'react-router-dom'

import Navbar from './components/Navbar'
import Map from './components/Map'
import Profile from './components/Profile'

export default () => (
  <Router>
    <Navbar>
    <Profile>
    <Switch>
    <Route path="/">
      <Map />
    </Route>

    </Switch>
    </Profile>
    </Navbar>
  </Router>

);
