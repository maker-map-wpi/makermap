import React from "react";
import {Menu, Icon, Button} from "semantic-ui-react"

export default class Titlebar extends React.Component {
  render() {
    return <Menu>
      <Button icon>
        <Icon name='hamburger'/>
      </Button>
    </Menu>
  }
}
