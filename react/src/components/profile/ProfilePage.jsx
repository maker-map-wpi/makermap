import React, {PropTypes} from 'react';
import ProfileArea from './ProfileArea';

export default class ProfilePage extends React.Component {
    render() {
        return (
            <div>
                <ProfileArea
                    username="kandonie"
                    emailAddress="kandonie@wpi.edu"
                />
            </div>
        );
    }
}

ProfilePage.propTypes = {
};

export default ProfilePage;