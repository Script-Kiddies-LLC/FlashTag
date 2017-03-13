import React, { Component } from 'react'
import {
  AppRegistry,
  StyleSheet,
  View,
  Dimensions,
  ScrollView,
  Text
} from 'react-native'
import Camera from 'react-native-camera';
import TabNavigator from 'react-native-tab-navigator';
import io from 'socket.io-client';
import MapView from 'react-native-maps';

const { width, height } = Dimensions.get('window')

window.navigator.userAgent = 'ReactNative'

export default class AwesomeProject extends Component {
  constructor (props) {
    super(props)
    this.state = {
      markers: [{
        title: 'Title',
        description: 'Description',
        latlng: {
          latitude: 37.7882511,
          longitude: -122.432
        }
      }],
    }
    this.initialPosition = null
    this.lastPosition = null
    this.socket = io('http://elfin.io/', {
      jsonp: false,
      transports: ['websocket'],
      secure: false
    })
    this.socket.on('connect', function () {
      console.log('CONNECTION SUCCESSFUL!!!')
      this.socket.emit('message', {data: 'data'})
    })
  }
  componentDidMount () {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        var initialPosition = JSON.stringify(position)
        console.log(width)
        this.map.animateToRegion({
          latitude: 37.78825,
          longitude: -122.4324,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0922 * (width / height)
        })
        this.setState({initialPosition})
      },
      (error) => window.alert(JSON.stringify(error)),
      {enableHighAccuracy: true, timeout: 5000, maximumAge: 60000}
    )
    this.watchID = navigator.geolocation.watchPosition((position) => {
      var lastPosition = JSON.stringify(position)
      this.setState({lastPosition})
    })
  }
  takePicture() {
    this.camera.capture()
      .then((data) => console.log(data))
      .catch(err => console.error(err));
  }
  render () {
    return (
      <View style={styles.container}>
        <Camera
            ref={(cam) => {
              this.camera = cam;
            }}
            style={styles.preview}
            aspect={Camera.constants.Aspect.fill}>
            <Text style={styles.capture} onPress={this.takePicture.bind(this)}>[CAPTURE]</Text>
            </Camera>
        <MapView
          style={styles.map}
          region={this.initialPosition}
          ref={ref => { this.map = ref }}
          initialRegion={{
            latitude: 37.7882511,
            longitude: -122.432,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421
          }}
        >
          {this.state.markers.map(function (marker, i) {
            return (
              <MapView.Marker
                coordinate={marker.latlng}
                title={marker.title}
                description={marker.description}
                key={i} />
            )
          })
        }
        </MapView>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF'
  },
  map: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center'
  },
  capture: {
    flex: 0,
    backgroundColor: '#fff',
    borderRadius: 5,
    color: '#000',
    padding: 10,
    margin: 40
  }
})

AppRegistry.registerComponent('AwesomeProject', () => AwesomeProject)
