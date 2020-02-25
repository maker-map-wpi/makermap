import React from "react";
import {Icon, Input, Dropdown} from "semantic-ui-react"

export default class DropdownSearch extends React.Component {
  constructor(){
    super()
  }

  render() {
    return    <Dropdown item text="Options">
    <Dropdown.Menu>
      <Input icon='search' iconPosition='left' className='search' />
      <Dropdown.Menu scrolling>

          {this.props.data.map((d) => (
            <Dropdown.Item key={d.idBuildings} text={d.Name} value={d.idBuildings}/>
          ))}


      </Dropdown.Menu>
    </Dropdown.Menu>
  </Dropdown>;
  }
}
