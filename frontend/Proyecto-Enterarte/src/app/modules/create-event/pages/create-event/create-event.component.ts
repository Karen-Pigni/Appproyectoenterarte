import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Event } from 'src/app/modules/events/interfaces/event';
import { EventsService } from 'src/app/modules/events/services/events.service';

@Component({
  selector: 'app-create-event',
  templateUrl: './create-event.component.html',
  styleUrls: ['./create-event.component.css']
})
export class CreateEventComponent implements OnInit {

  eventForm !: FormGroup;
  invalidForm : boolean = false;

  patternURL:string = "[-a-zA-Z0-9@:%_\\+.~#?&//=]{2,256}\\.[a-z]{2,4}\\b(\\/[-a-zA-Z0-9@:%_\\+.~#?&//=]*)?"

  constructor (private formBuilder: FormBuilder,
               private eventService: EventsService) {  }


  ngOnInit(): void {
    this.eventForm = this.formBuilder.group({
      name: ['', [Validators.required]],
      date: ['',[Validators.required]],
      price: ['',[Validators.required]],
      category: ['',[Validators.required]],
      gender: ['',[Validators.required]],
      description: ['',[Validators.required]],
      province: ['',[Validators.required]],
      city: ['',[Validators.required]],
      street: ['',[Validators.required]],
      number: ['',[Validators.required]],
      instagram: ['',[Validators.pattern(this.patternURL)]],
      facebook: ['',[Validators.pattern(this.patternURL)]],
      website: ['',[Validators.pattern(this.patternURL)]],
      image: ['', [Validators.required]]

      });
  }

  resetForm ():void {
    this.eventForm.reset();
    this.invalidForm=false
  }


  onSubmit ():void {
    if(this.eventForm.invalid) {
    this.invalidForm=true     
    } else {     
      const event: Event = this.eventForm.value;   
      this.eventService.addEvent(event).subscribe();
      this.eventForm.reset();
      this.invalidForm = false;   
    
    }
  } 

  hideErrorMessage () {   
    this.invalidForm=false
  } 

}
