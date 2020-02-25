import React from "react";
import Titlebar from './map/Titlebar'
import Pin from './map/Pin'
import {Container, Input, Dropdown} from "semantic-ui-react"
import ReactMapGL, {Marker} from 'react-map-gl';



const mapboxToken = "pk.eyJ1IjoibWFrZXJtYXAtd3BpIiwiYSI6ImNrNzI0dGM4ajBjZ2kzZm5tY3VuZWFsZXAifQ.H7Jee_QDv1lO2EmDvCcCUw"

export default class Map extends React.Component {
  constructor(props) {
    //make a blank articles list in state
    super(props)
    this.state = {
      viewport: {
        width: '100%',
        height: '100%',
        latitude: 42.2736,
        longitude: -71.8063,
        zoom: 16
      }, markers:this.props.data
    }
  }



  render() {
    return  <div>
    <Titlebar data={this.props.data} click={this.props.click}/>
    <ReactMapGL
            {...this.state.viewport}
            onViewportChange={(viewport) => this.setState({viewport})}
          mapboxApiAccessToken={mapboxToken}
          mapStyle="mapbox://styles/mapbox/streets-v11"
          >
          {this.props.data.map(b => (
            <Marker key={b.idBuildings} latitude={b.Latitude} longitude={b.Longitude} offsetLeft={-20} offsetTop={-10}>
              <Pin onClick={() => this.setState({ popupInfo: b })} />
            </Marker>))
        }

    </ReactMapGL>
    </div>;
  }
}
