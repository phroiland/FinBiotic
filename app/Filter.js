
import React from 'react';

export default class FilterAndAdd extends React.Component {

    constructor(props) {
        super(props);
    }

    onAdd() {
        this.props.OnAdd();
    }

    handleFilterChange(e) {
        this.props.OnFilter(e.target.value);
    }

    render() {
        return(<form>
                    <div className="form-group col-md-4">
                        <input type="text" className="form-control" id="filter" placeholder="Search"
                              onChange={this.handleFilterChange.bind(this)} />
                    </div>
                    <div className="col-md-2">
                         <button type="button" className="btn btn-primary" onClick={this.onAdd.bind(this)}>
                            <span className="glyphicon-plus" aria-hidden="true"></span>
                        </button>
                    </div>
                </form>);
    }
}
