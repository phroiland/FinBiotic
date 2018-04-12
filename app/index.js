
require('bootstrap/dist/css/bootstrap.min.css');
require('./css/main.css');
import React from 'react';
import ReactDOM from 'react-dom';
import ManageMarket from './ManageMarket.js';
ReactDOM.render(
  <ManageMarket />,
  document.getElementById('app')
);
