import React from "react";
import {Menu, Icon, Button, Search} from "semantic-ui-react"
import DropdownSearch from "./DropdownSearch"
export default class Titlebar extends React.Component {
  render() {
    return <Menu borderless fixed="top">
      <Menu.Item as={Button} onClick={this.props.click}>
          <Icon name='bars'/>
      </Menu.Item>
      <DropdownSearch data={this.props.data}/>
    </Menu>
  }
}
