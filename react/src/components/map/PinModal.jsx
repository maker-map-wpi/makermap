import React from 'react';
import {Button} from 'semantic-ui-react'
export default class PinModal extends React.Component {

  render() {
    return (
      <div>
        <h3>{this.props.name}</h3>
        <h4>Hours: {this.props.hours}</h4>
      </div>
    );
  }
}
