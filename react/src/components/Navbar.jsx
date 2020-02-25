import React from "react";
import {Menu, Icon, Image, Sidebar} from "semantic-ui-react"
import {Link} from "react-router-dom"
import "../css/navbar.css"

export default class Navbar extends React.Component {
  render() {
    return <Sidebar.Pushable>
      <Sidebar as={Menu} width='thin' size='small' visible={true} className="custom" inverted fixed='left' vertical borderless>
        <Menu.Item header>
          <Image src='https://upload.wikimedia.org/wikipedia/en/1/1b/WPI_logo.png' size='mini' spaced='right'/>
          MakerMap
        </Menu.Item>
        <Menu.Menu>
          <Menu.Item as={'a'} href='https://github.com/makermap/makermap'>
            Github
            <Icon name='github'/>
          </Menu.Item>
        </Menu.Menu>
        <Menu.Item header>Pages</Menu.Item>
        <Menu.Menu>
          <Menu.Item as={Link} name='Map' to='/'/>
          <Menu.Item as={Link} name='About The Project' to='/about'/>
        </Menu.Menu>
      </Sidebar>
      <Sidebar.Pusher>
        {this.props.children}
      </Sidebar.Pusher>
    </Sidebar.Pushable>;
  }
}
