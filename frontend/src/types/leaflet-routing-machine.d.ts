import * as L from 'leaflet';

declare module 'leaflet' {
  namespace Routing {
    function control(options: any): any;
  }

  namespace routing {
    interface ControlOptions {
      waypoints: L.LatLng[];
      routeWhileDragging?: boolean;
      show?: boolean;
      // add other options you need
    }
  }

  const Routing: {
    control(options: any): L.Control;
  }
}
