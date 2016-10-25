import { Webcast } from './webcast';
import { WEBCASTS } from './mock-webcasts';
import { Injectable } from '@angular/core';

@Injectable()
export class WebcastService {
  getWebcasts(): Promise<Webcast[]> {
    return Promise.resolve(WEBCASTS);
  }

  getWebcast(id: number): Promise<Webcast> {
    return this.getWebcasts()
               .then(webcasts => webcasts.find(webcast => webcast.id === id));
  }
}
