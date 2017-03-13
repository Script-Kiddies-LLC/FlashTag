import React from 'react'
import {
  AppRegistry,
} from 'react-native'

import Root from './App/Root'

window.navigator.userAgent = 'ReactNative'

AppRegistry.registerComponent('App', () => Root)
