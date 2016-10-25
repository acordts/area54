import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Webcast } from './webcast';
import { WebcastService } from './webcast.service';

@Component({
  moduleId: module.id,
  selector: 'ondemand',
  templateUrl: 'ondemand.component.html',
})


export class OnDemandComponent implements OnInit {
  webcasts: Webcast[];
  selectedWebcast: Webcast;

  constructor(
    private router: Router,
    private webcastService: WebcastService) { }

  getWebcasts(): void {
    this.webcastService.getWebcasts()
        .then(webcasts => this.webcasts = webcasts.filter(webcast => webcast.ondemand));
  }

  ngOnInit(): void {
    this.getWebcasts();
  }

  onSelect(webcast: Webcast): void {
    this.selectedWebcast = webcast;
  }

  gotoDetail(): void {
    this.router.navigate(['/webcast', this.selectedWebcast.id]);
  }
}
