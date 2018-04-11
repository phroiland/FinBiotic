
require('bootstrap/dist/css/bootstrap.min.css');
require('./css/main.css');
import React from 'react';
import ReactDOM from 'react-dom';
import ManageCurrencyPair from './ManageCurrencyPair.js';
ReactDOM.render(
  <ManageCurrencyPair />,
  document.getElementById('app')
);