import { Component, OnInit }      from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location }               from '@angular/common';

import { Webcast }         from './webcast';
import { WebcastService }  from './webcast.service';
@Component({
  moduleId: module.id,
  selector: 'webcast-detail',
  templateUrl: 'webcast-detail.component.html',
})
export class WebcastDetailComponent implements OnInit {
  webcast: Webcast;

  constructor(
    private webcastService: WebcastService,
    private route: ActivatedRoute,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.route.params.forEach((params: Params) => {
      let id = +params['id'];
      this.webcastService.getWebcast(id)
        .then(webcast => this.webcast = webcast);
    });
  }

  goBack(): void {
    this.location.back();
  }
}
