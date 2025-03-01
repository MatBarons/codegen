import {Directive, EventEmitter, HostListener, Output} from "@angular/core";
/**
 * Drag and drop directive that can be applied to a tag and detect when something is dragged across it (both enter and exit) and is dropped in it
 */
@Directive({
  selector: '[fileDragDrop]'
})
export class FileDragDropDirective {
  @Output() filesChangeEmitter : EventEmitter<DragEvent> = new EventEmitter();
  @Output() isDragging : EventEmitter<boolean> = new EventEmitter();

  constructor() { }

  @HostListener('dragover', ['$event']) public onDragOver(evt : DragEvent){
    evt.preventDefault();
    evt.stopPropagation();
    this.isDragging.emit(true)
  }

  @HostListener('dragleave', ['$event']) public onDragLeave(evt : DragEvent){
    evt.preventDefault();
    evt.stopPropagation();
    this.isDragging.emit(false)
  }

  @HostListener('drop', ['$event']) public onDrop(evt : DragEvent){
    evt.preventDefault();
    evt.stopPropagation();
    this.filesChangeEmitter.emit(evt);
    this.isDragging.emit(false)
  }
}
