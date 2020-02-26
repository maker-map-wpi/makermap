import React from 'react'
import { Divider, Grid, Image, Segment, Icon } from 'semantic-ui-react'

export default class ProfilePage extends React.Component {
    render() {
        return (
            <div>
                <Segment vertical>
                    <Image src="/kristen.png" className="ui small image"/>
                </Segment>
                <Segment vertical>
                    <h1> &nbsp; Kristen Andonie {this.props.name}</h1>
                </Segment>
                <Segment vertical>
                    <p> &nbsp;&nbsp;&nbsp;&nbsp; <Icon name='mail' /> kandonie@wpi.edu {this.props.email}</p>
                    <p> &nbsp;&nbsp;&nbsp;&nbsp; <Icon name='phone' /> (305) 798 - 8475</p>
                </Segment>
            </div>
        );
    }
}