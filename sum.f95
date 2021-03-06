subroutine sum(array, array_size, array_sum)

    integer                                      :: i
    integer, intent(in) :: array_size
    integer, dimension(array_size), intent(in)  :: array
    integer, intent(out)                         :: array_sum

    do i = 1, array_size
        array_sum = array_sum + array(i)
    end do

end subroutine
