import React from 'react';

export default class ProfilePage extends React.Component {
    render() {
        return (
            <div>
                <h1>Kristen Andonie {this.props.name}</h1>

                <ul>
                    <li>Email address: kandonie@wpi.edu {this.props.email}</li>
                </ul>
            </div>
        );
    }
}