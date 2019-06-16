import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import ServiceHeader from "./ServiceHeader/ServiceHeader";
import ServiceMenu from "./ServiceMenu/ServiceMenu";
import { Grid, GridColumn, Segment } from "semantic-ui-react";

class App extends Component {
    render() {
        const header_bg_color = "grey";
  const menu_bg_color = "teal";
  const max_grid_col_width = 10;

        return (
    <div className="App">
      <Grid>
        <GridColumn width="3" />
        <GridColumn width="10">
          <Segment color="teal" inverted>
            <ServiceHeader
              header_bg_color={header_bg_color}
              max_grid_col_width={max_grid_col_width}
            />
            <ServiceMenu menu_bg_color={menu_bg_color} />
          </Segment>
        </GridColumn>
        <GridColumn width="3" />
      </Grid>
    </div>
  );
    }
}

ReactDOM.render(<App></App>, document.getElementById('app'));