from rest_framework import filters


class IsActiveFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_active = request.query_params.get('is_active', 'true')
        is_active = is_active.lower() == 'true'

        return queryset.filter(item__is_active=is_active)


class DealTypeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        result = queryset
        user = request.user

        deal_type = view.kwargs.get('deal_type')
        if deal_type == 'personal':
            result = result.filter(item__owner=user)
        elif deal_type == 'following':
            result = result.filter(buyer=user)

        return result
