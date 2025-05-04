import { Component, DestroyRef, OnInit } from '@angular/core';
import { component_nameService } from '../component_name.service';
import {component_name} from '../models/component_name';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'project_name-component_name-table',
  templateUrl: './component_name-table.component.html',
  styleUrl: './component_name-table.component.scss'
})
export class component_nameComponent implements OnInit{
  component_name: Array<component_name> = [];
  /*Insert variables here */
  
  constructor(
    private component_nameService: component_nameService,
    private route: ActivatedRoute,
    private readonly router: Router,
  ) {}

  /*Insert methods here */

  get_component_name() {
    this.component_nameService
      .getcomponent_name(/*insert filters here */)
      .subscribe((r: component_name) => {
        this.component_name = r;
      });
  }

  goDetail (code: string): void {
    this.router.navigate([code], { relativeTo: this.route })
  }
}
