import React from 'react'
import { Divider, Grid, Image, Segment, Icon } from 'semantic-ui-react'

export default class ProfilePage extends React.Component {
    render() {
        return (
            <div class="ui two column stackable grid">
                <Segment.Group>
                    <Segment>
                        <Image src="https://media-exp1.licdn.com/dms/image/C5603AQGAdri1_rnrTg/profile-displayphoto-shrink_200_200/0?e=1588204800&v=beta&t=5PKKEDJojRcspVl_vcjbN0C7ZP6DebuWaCwld53cDU0"
                               className="ui small image"></Image>
                    </Segment>
                    <Segment>
                        <h1> Kristen Andonie {this.props.name}</h1>
                    </Segment>
                    <Segment>
                        <p> I'm a robotics engineering and computer science double major. I was on the MakerMap IQP team.</p>
                            <p> I'm an RBE1001 SA, and my hobbies are hiking, climbing, and reading. I'm also Vice President of Rho Beta Epsilon. </p>
                    </Segment>
                    <Segment>
                        <p> <Icon name='mail' /> kandonie@wpi.edu {this.props.email}</p>
                        <p> <Icon name='phone' /> (305) 798 - 8475</p>
                        <p> <Icon name='home' /> East Hall 314</p>
                    </Segment>
                </Segment.Group>

            </div>
        );
    }
}